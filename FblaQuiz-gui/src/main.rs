use FblaQuiz_gui::submit_requests::submit_login;
use gtk::prelude::*;
use gio::prelude::*;
use gtk::{self, Application, ApplicationWindow, Button, Label, Entry, Window};
use FblaQuiz_gui::submit_requests::*;

fn main() {
    if gtk::init().is_err() {
        println!("Failed to initialize GTK.");
        return;
    }
    let glade_src = include_str!("Test.glade");

    let builder = gtk::Builder::from_string(glade_src);


    let login_window: Window = builder.get_object("window_main").unwrap();
    let main_window: Window = builder.get_object("window_home").unwrap();
    let username_field: Entry = builder.get_object("EmailBox").unwrap();
    let password_field: Entry = builder.get_object("PasswordBox").unwrap();
    let submit_button: Button = builder.get_object("SubmitButton").unwrap();
    let key_label: Label = builder.get_object("Key").unwrap();
    let passwordLabel: Label = builder.get_object("Password").unwrap();
    let emailLabel: Label = builder.get_object("Email").unwrap();
    
    login_window.show_all();

    submit_button.clone().connect_clicked(move |_| {
        let username = username_field.get_text().to_string();
        let password = password_field.get_text().to_string();
        
        println!("{}, {}", &username, &password);

        key_label.set_text(submit_login(username.as_str(), password.as_str()).unwrap().as_str());

        username_field.hide();
        password_field.hide();
        submit_button.hide();
        emailLabel.hide();
        passwordLabel.hide();

    });


    gtk::main();
}
