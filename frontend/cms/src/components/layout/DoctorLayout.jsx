import Header from "../doctor/Header";
import DoctorSidebar from "../doctor/DoctorSidebar";
import "./DoctorLayout.css";

function DoctorLayout({ children }) {
    return (
        <div className="doctor-layout">

            <Header />

            <div className="doctor-layout-body">
                <DoctorSidebar />

                <main className="doctor-main-content">
                    {children}
                </main>
            </div>

        </div>
    );
}

export default DoctorLayout;