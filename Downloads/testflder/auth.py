cat > auth.py << 'EOF'
import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def check_login(user, password):
    if user == "admin" and password == "admin123":
        return True
    return False
EOF