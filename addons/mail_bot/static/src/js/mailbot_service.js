eagle.define('mail_bot.MailBotService', function (require) {
"use strict";

var AbstractService = require('web.AbstractService');
var core = require('web.core');
var session = require('web.session');

var _t = core._t;

var MailBotService =  AbstractService.extend({
    /**
     * @override
     */
    start: function () {
        this._hasRequest = (window.Notification && window.Notification.permission === "default") || false;
        if ('eaglebot_initialized' in session && ! session.eaglebot_initialized) {
            this._showEaglebotTimeout();
        }
    },

    //--------------------------------------------------------------------------
    // Public
    //--------------------------------------------------------------------------

    /**
     * Get the previews related to the EagleBot (conversation not included).
     * For instance, when there is no conversation with EagleBot and EagleBot has
     * a request, it should display a preview in the systray messaging menu.
     *
     * @param {string|undefined} [filter]
     * @returns {Object[]} list of objects that are compatible with the
     *   'mail.Preview' template.
     */
    getPreviews: function (filter) {
        if (!this.isRequestingForNativeNotifications()) {
            return [];
        }
        if (filter && filter !== 'mailbox_inbox') {
            return [];
        }
        var previews = [{
            title: _t("EagleBot has a request"),
            imageSRC: "/mail/static/src/img/eaglebot.png",
            status: 'bot',
            body:  _t("Enable desktop notifications to chat"),
            id: 'request_notification',
            unreadCounter: 1,
        }];
        return previews;
    },
    /**
     * Tell whether EagleBot is requesting to enable push notifications.
     *
     * @returns {boolean}
     */
    isRequestingForNativeNotifications: function () {
        return this._hasRequest;
    },
    /**
     * Called when user either accepts or refuses push notifications.
     */
    removeRequest: function () {
        this._hasRequest = false;
    },

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @private
     */
    _showEaglebotTimeout: function () {
        var self = this;
        setTimeout(function () {
            session.eaglebot_initialized = true;
            self._rpc({
                model: 'mail.channel',
                method: 'init_eaglebot',
            });
        }, 2*60*1000);
    },
});

core.serviceRegistry.add('mailbot_service', MailBotService);
return MailBotService;

});
