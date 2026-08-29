import { NavLink } from "react-router-dom";
import "./Sidebar.css";

function Sidebar() {
    return (
        <aside className="sidebar">

            <nav className="sidebar-menu">

                <NavLink
                    to="/dashboard"
                    className={({ isActive }) =>
                        isActive ? "menu-item active" : "menu-item"
                    }
                >
                    <span>📊</span>
                    <span>Dashboard</span>
                </NavLink>

                <NavLink
                    to="/patients"
                    className={({ isActive }) =>
                        isActive ? "menu-item active" : "menu-item"
                    }
                >
                    <span>👥</span>
                    <span>Patients</span>
                </NavLink>

            </nav>

        </aside>
    );
}

export default Sidebar;