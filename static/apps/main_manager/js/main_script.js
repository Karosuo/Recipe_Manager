var recipe_manager = new Vue({
    delimiters: ['[[', ']]'],
    el: "#base_recipe_manager",
    vuetify: new Vuetify({
        theme: {
            dark: false
        }
    }),
    data: {
        app_header_title: "Recipe Manager",
        drawer_data: {
            flag: true,
            items: [
                {
                    "title": "Shopping List",
                    "target": shopping_list_url,
                    "icon": "shopping_cart",
                    "disabled": false
                },
                {
                    "title": "Upload Data",
                    "target": shopping_list_url,
                    "icon": "playlist_add",
                    "disabled": true
                },
                {
                    "title": "Inventory Updater",
                    "target": shopping_list_url,
                    "icon": "remove_from_queue",
                    "disabled": true
                },
            ],
        },
        shopping_list_data: {
            selected: [],
            cart_items: [
                {
                    "GroupTitle": "Verduras",
                    "GroupItems": [
                        {
                            "name": "Platano",
                            "text_qty": "10 KG"
                        }
                    ]
                },
                {
                    "GroupTitle": "Carnes",
                    "GroupItems": [
                        {
                            "name": "Bisteck",
                            "text_qty": "2 KG"
                        }
                    ]
                }
            ]
        },
    },
    watch: {},
    methods: {}

});