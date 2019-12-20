eagle.define('iap.redirect_eagle_credit_widget', function(require) {
"use strict";

var AbstractAction = require('web.AbstractAction');
var core = require('web.core');


var IapEagleCreditRedirect = AbstractAction.extend({
    template: 'iap.redirect_to_eagle_credit',
    events : {
        "click .redirect_confirm" : "eagle_redirect",
    },
    init: function (parent, action) {
        this._super(parent, action);
        this.url = action.params.url;
    },

    eagle_redirect: function () {
        window.open(this.url, '_blank');
        this.do_action({type: 'ir.actions.act_window_close'});
        // framework.redirect(this.url);
    },

});
core.action_registry.add('iap_eagle_credit_redirect', IapEagleCreditRedirect);
});
