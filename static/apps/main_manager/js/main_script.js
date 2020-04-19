axios.defaults.headers.post["X-CSRFToken"] = base_token;

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
                    "target": load_data_url,
                    "icon": "playlist_add",
                    "disabled": false
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
        load_data_info: {
            recipe_file_valid: false,
            plan_file_valid: false,
            inventory_file_valid: false,
            selected_file_ref: "",
            loading_files: false
        },
        snackbar_props: {
            flag: false,
            timeout: 2500,
            color: "red darken-4",
            text: "",
            close_btn_color: "white"
        },
    },
    watch: {},
    methods: {
        validate_recipes_file_format: function(){
            return true;
        },
        validate_plan_file_format: function(){
            return true;
        },
        validate_cinventory_file_format: function () {
            return true;
        },
        change_upload_tab: function (tab_idx) {
            console.log(tab_idx);
            if(tab_idx === 0)
            {
                this.load_data_info.selected_file_ref = "recipes_file";
            }
            else if(tab_idx === 1)
            {
                this.load_data_info.selected_file_ref = "plan_file";
            }
            else if(tab_idx === 2)
            {
                this.load_data_info.selected_file_ref = "inventory_file";
            }
        },
        upload_data_file: function () {
            let formData = new FormData();
            let target_file_ref = this.load_data_info.selected_file_ref;
            formData.append(target_file_ref, this.$refs[target_file_ref].lazyValue);

            this.load_data_info.loading_files = true;

            axios.post(
                upload_data_files_url,
                formData,
                {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }
            ).then(
                response => {
                    this.snackbar_props.flag = true;
                    this.snackbar_props.text = "Correctly Added "+target_file_ref;
                    this.snackbar_props.color = "success";
                }
            ).catch(
                response => {
                    this.snackbar_props.flag = true;
                    this.snackbar_props.text = "Error parsing the files";
                    this.snackbar_props.color = "red darken-4";
                    this.snackbar_props.timeout = 4500;
                }
            ).finally(
                () => {this.load_data_info.loading_files = false;}
            );
        }

    }

});