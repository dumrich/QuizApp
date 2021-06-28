use druid::widget::{Button, Flex, Label, TextBox};
use druid::{LocalizedString, Widget, WidgetExt, UnitPoint};
use crate::core::UserState;


pub fn ui_builder() -> impl Widget<UserState> {
    // The label text will be computed dynamically based on the current locale and count
    let name_textbox = TextBox::new()
        .with_placeholder("Username")
        .with_text_size(18.0)
        .fix_width(200.0)
        .lens(UserState::name);
    
    let password_textbox = TextBox::new()
        .with_placeholder("Password")
        .with_text_size(18.0)
        .fix_width(200.0)
        .lens(UserState::password);

    let submit_button = Button::new("Submit")
        .on_click(|_ctx, data: UserState, _env| println!("{}", *data.name.into()));
        

    Flex::column()
        .with_child(name_textbox)
        .with_spacer(20.0)
        .with_child(password_textbox)
        .align_vertical(UnitPoint::CENTER)
}
