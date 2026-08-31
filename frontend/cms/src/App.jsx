// import { Routes, Route } from "react-router-dom";
// import DoctorLayout from "./components/layout/DoctorLayout";

// function Dashboard() {
//     return <h1>Dashboard</h1>;
// }

// function Patients() {
//     return <h1>Patients</h1>;
// }

// function App() {
//     return (
//         <Routes>
//             <Route element={<DoctorLayout />}>

//                 <Route path="/" element={<Dashboard />} />
//                 <Route path="/patients" element={<Patients />} />

//             </Route>
//         </Routes>
//     );
// }

// export default App;
import { Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import PatientTable from "./components/doctor/PatientTable";
import DoctorLayout from "./components/layout/DoctorLayout";
import ReceptionistLayout from "./components/layout/ReceptionistLayout";
import DoctorDashboard from "./pages/Doctor/DoctorDashboard";
import ReceptionistDashboard from "./pages/Receptionist/ReceptionistDashboard";
import ReceptionistPatientList from "./pages/Receptionist/ReceptionistPatientList";
import AdminDashboard from "./pages/Admin/AdminDashboard";
import AdminLayout from "./components/layout/AdminLayout";
import AdminStaffList from "./pages/Admin/AdminStaffList";
function Dashboard() {
    return <h1>Doctor Dashboard</h1>;
}

function Patients() {
    return <>    <h1>Patients</h1> <PatientTable /></>;
}


function App() {
    return (
        <Routes>

            {/* Login */}
            <Route path="/login" element={<Login />} />

            {/* Doctor */}
            <Route element={<DoctorLayout />}>

                <Route path="/" element={<DoctorDashboard />} />
                <Route path="/patients" element={<Patients />} />

            </Route>

            {/* Receptionist */}
            <Route element={<ReceptionistLayout />}>

                <Route
                    path="/receptionist"
                    element={<ReceptionistDashboard />}
                />
                
                    <Route
                    path="/patientList"
                    element={<ReceptionistPatientList />}
                />

            </Route>
          <Route element={<AdminLayout />}>

    <Route
        path="/admin"
        element={<AdminDashboard />}
    />

    {/* <Route
        path="/admin/patients"
        element={<AdminPatientList />}
    /> */}

    <Route
        path="/admin/staff"
        element={<AdminStaffList />}
    />

</Route>
        </Routes>
    );
}

export default App;