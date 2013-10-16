Vaultier.WorkspaceIndexRoute = Ember.Route.extend({
    model: function (params) {
        var store = this.get('store');
        var promise = store.find('Workspace');
        return promise;
    }
});


Vaultier.WorkspaceIndexController = Ember.ArrayController.extend({
    breadcrumbs: Vaultier.utils.Breadcrumbs.create()
        .addLink('WorkspaceIndex', 'Workspaces'),

    actions: {
        createWorkspace: function () {
            this.set('sortAscending', !this.get('sortAscending'));
        }
    }
});

Vaultier.WorkspaceIndexView = Ember.View.extend({
    templateName: 'Workspace/Index',
    layoutName: 'Layout/LayoutStandard'
});

Vaultier.WorkspaceIndexItemView = Ember.View.extend({
    templateName: 'Workspace/IndexItem'
});
