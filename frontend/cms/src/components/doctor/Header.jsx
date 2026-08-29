import "./Header.css";
import hospitalLogo from "../../assets/hospital_logo.png";
import profilePic from "../../assets/profilePic.png";

function Header() {
    return (
        <header className="header">

            {/* Left side */}
            <div className="header-left">
                <img
                    src={hospitalLogo}
                    alt="Hospital Logo"
                    className="hospital-logo"
                />

                <h2>City Care Hospital</h2>
            </div>

            {/* Right side */}
            <div className="header-right">
                <img
                    src={profilePic}
                    alt="Profile"
                    className="profile-pic"
                />

                <span className="user-name">
                    Dr. John Doe
                </span>
            </div>

        </header>
    );
}

export default Header;