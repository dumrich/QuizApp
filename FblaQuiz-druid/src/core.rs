use druid::{AppLauncher, PlatformError, WindowDesc, Data, Lens};
use crate::ui;

pub struct App<'a> {
    title: &'a str,
    width: u32,
    height: u32,
}


#[derive(Clone, Data, Lens)]
pub struct UserState {
    name: String,
    password: String
}

impl<'a> App<'a> {
    pub fn new(title: &'a str, width: u32, height: u32) -> App<'a> {
        // Spawn new App
        App {
            title,
            width,
            height
        }
        
    }
    pub fn spawn(&self) -> Result<(), PlatformError> {
        // Launch App struct
        let window = WindowDesc::new(ui::ui_builder())
            .title(self.title)
            .window_size((self.width as f64, self.height as f64));

        let initial_state: UserState = UserState {
            name: "".into(),
            password: "".into()
        };

        AppLauncher::with_window(window)
            .log_to_console()
            .launch(initial_state)
    } 
}
