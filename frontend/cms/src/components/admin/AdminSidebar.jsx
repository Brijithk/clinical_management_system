
import { NavLink } from "react-router-dom";
import "./AdminSidebar.css";

import dashboardIcon from "../../assets/dashboard.png";
import patientsIcon from "../../assets/online-booking.png";

function AdminSidebar() {
    return (
        <aside className="admin-sidebar">

            <nav className="admin-sidebar-menu">

                <NavLink
                    to="/"
                    className={({ isActive }) =>
                        isActive
                            ? "admin-menu-item active"
                            : "admin-menu-item"
                    }
                >
                    <img src={dashboardIcon} alt="" />
                    <span>Dashboard</span>
                </NavLink>

                <NavLink
                    to="/admin/staff"
                    className={({ isActive }) =>
                        isActive
                            ? "admin-menu-item active"
                            : "admin-menu-item"
                    }
                >
                    <img src={patientsIcon} alt="" />
                    <span>Staff List</span>
                </NavLink>

                <NavLink
                    to="/patients"
                    className={({ isActive }) =>
                        isActive
                            ? "admin-menu-item active"
                            : "admin-menu-item"
                    }
                >
                    <img src={patientsIcon} alt="" />
                    <span>Patients</span>
                </NavLink>

                <NavLink
                    to="/patients"
                    className={({ isActive }) =>
                        isActive
                            ? "admin-menu-item active"
                            : "admin-menu-item"
                    }
                >
                    <img src={patientsIcon} alt="" />
                    <span>Billing</span>
                </NavLink>

            </nav>

        </aside>
    );
}

export default AdminSidebar;

