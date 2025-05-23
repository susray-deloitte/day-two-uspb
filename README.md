# day-two-uspb

A simple Flask application demonstrating a contact form with input validation, modularized using Blueprints, and environment-based configuration.

## Directory Structure

```
day-two-uspb/
│
├── app.py                  # Main Flask app, registers Blueprints and loads config
├── contact/
│   └── routes.py           # Blueprint for contact form routes and validation logic
├── templates/
│   └── contact.html        # Jinja2 template for the contact form UI
├── .env                    # (Optional) Environment variables for configuration
└── README.md               # Project documentation (this file)
```

## File Explanations

- **app.py**: Entry point for the Flask app; sets up configuration and registers the contact Blueprint.
- **contact/routes.py**: Contains the Blueprint with all routes and validation logic for the contact form.
- **templates/contact.html**: Jinja2 template for rendering the contact form and displaying messages.
- **.env**: (Optional) Stores environment variables like `SECRET_KEY` for configuration.
- **README.md**: Project overview, directory structure, and file explanations.

---
