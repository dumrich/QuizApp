mod ui;
mod core;
use crate::core::App;
use druid::PlatformError;

fn main() -> Result<(), PlatformError> {
    let app = App::new("Hello World", 500, 500);

    app.spawn()
}
