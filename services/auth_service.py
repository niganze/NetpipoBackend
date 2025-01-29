from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app.config["JWT_SECRET_KEY"] = "supersecretkey"
jwt = JWTManager(app)

# Restrict endpoints using `@jwt_required`
