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
import Login from "./pages/Login";

function App() {
    return <Login />;
}

export default App;