#!/bin/sh

set -e

ODOO_CONFIGURATION_DIR=/etc/eagle
ODOO_CONFIGURATION_FILE=$ODOO_CONFIGURATION_DIR/eagle.conf
ODOO_DATA_DIR=/var/lib/eagle
ODOO_GROUP="eagle"
ODOO_LOG_DIR=/var/log/eagle
ODOO_LOG_FILE=$ODOO_LOG_DIR/eagle-server.log
ODOO_USER="eagle"

if ! getent passwd | grep -q "^eagle:"; then
    groupadd $ODOO_GROUP
    adduser --system --no-create-home $ODOO_USER -g $ODOO_GROUP
fi
# Register "$ODOO_USER" as a postgres user with "Create DB" role attribute
su - postgres -c "createuser -d -R -S $ODOO_USER" 2> /dev/null || true
# Configuration file
mkdir -p $ODOO_CONFIGURATION_DIR
# can't copy debian config-file as addons_path is not the same
if [ ! -f $ODOO_CONFIGURATION_FILE ]
then
    echo "[options]
; This is the password that allows database operations:
; admin_passwd = admin
db_host = False
db_port = False
db_user = $ODOO_USER
db_password = False
addons_path = /usr/lib/python3.7/site-packages/eagle/addons
" > $ODOO_CONFIGURATION_FILE
    chown $ODOO_USER:$ODOO_GROUP $ODOO_CONFIGURATION_FILE
    chmod 0640 $ODOO_CONFIGURATION_FILE
fi
# Log
mkdir -p $ODOO_LOG_DIR
chown $ODOO_USER:$ODOO_GROUP $ODOO_LOG_DIR
chmod 0750 $ODOO_LOG_DIR
# Data dir
mkdir -p $ODOO_DATA_DIR
chown $ODOO_USER:$ODOO_GROUP $ODOO_DATA_DIR

INIT_FILE=/lib/systemd/system/eagle.service
touch $INIT_FILE
chmod 0700 $INIT_FILE
cat << EOF > $INIT_FILE
[Unit]
Description=Eagle Open Source ERP and CRM
After=network.target

[Service]
Type=simple
User=eagle
Group=eagle
ExecStart=/usr/bin/eagle --config $ODOO_CONFIGURATION_FILE --logfile $ODOO_LOG_FILE
KillMode=mixed

[Install]
WantedBy=multi-user.target
EOF
