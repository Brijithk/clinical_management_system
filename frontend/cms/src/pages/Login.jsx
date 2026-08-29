import "./Login.css";
import logo from "../assets/hospital_logo.png";
function Login() {
    return (
        <div className="login-page">

            <div className="login-card">

                <div className="login-logo">
                    <img src={logo} alt="Hospital" />
                </div>

                <h2>Kims</h2>
                <p>Clinical Management System</p>

                <form>
                    <div className="input-group">
                        <label>Username</label>
                        <input
                            type="text"
                            placeholder="Enter username"
                        />
                    </div>

                    <div className="input-group">
                        <label>Password</label>
                        <input
                            type="password"
                            placeholder="Enter password"
                        />
                    </div>

                    <button type="submit">
                        Login
                    </button>
                </form>

            </div>

        </div>
    );
}

export default Login;