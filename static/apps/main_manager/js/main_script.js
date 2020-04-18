var recipe_manager = new Vue({
    delimiters: ['[[', ']]'],
    el: "#base_recipe_manager",
    vuetify: new Vuetify({
        theme: {
            dark: false
        }
    }),
    data: {
        drawer_data: {
            flag: true,
            items: []
        }

    },
    watch: {},
    methods: {}

});