(function () {
"use strict";

eagle.__DEBUG__.didLogInfo.then(function () {
    var modulesInfo = eagle.__DEBUG__.jsModules;

    QUnit.module('Eagle JS Modules');

    QUnit.test('all modules are properly loaded', function (assert) {
        assert.expect(2);

        assert.deepEqual(modulesInfo.missing, [],
            "no js module should be missing");
        assert.deepEqual(modulesInfo.failed, [],
            "no js module should have failed");
    });
});
})();
