pub mod submit_requests {
    use std::collections::HashMap;
    use reqwest;
    use tokio;
    use serde_json;

    #[tokio::main]
    pub async fn submit_login(username: &str, password: &str) -> Result<String, reqwest::Error> {
        let mut data_map = HashMap::new();
        data_map.insert("username", "");
        data_map.insert("email", username);
        data_map.insert("password", password);

        let payload = serde_json::json!({
            "username": "",
            "email": username,
            "password": password
        });


        let client = reqwest::Client::new();
        let res = client.post("http://127.0.0.1:8000/api/rest-auth/login/")
            .json(&payload)
            .send()
            .await?
            .text()
            .await?;

        Ok(res)
    }

}
