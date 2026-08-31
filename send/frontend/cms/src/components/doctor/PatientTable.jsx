import { useState } from "react";
import "./PatientTable.css";

function PatientTable() {

    const [showFilter, setShowFilter] = useState(false);
    const [selectedFilter, setSelectedFilter] = useState("All");
    const [searchTerm, setSearchTerm] = useState("");

    const patients = [
        {
            name: "John Doe",
            age: 32,
            condition: "Fever",
            date: "29 Aug 2026",
            status: "Pending",
        },
        {
            name: "Mary Thomas",
            age: 45,
            condition: "Diabetes",
            date: "29 Aug 2026",
            status: "In progress",
        },
        {
            name: "David Wilson",
            age: 28,
            condition: "Headache",
            date: "28 Aug 2026",
            status: "Done",
        },
        {
            name: "Sarah Joseph",
            age: 51,
            condition: "Blood Pressure",
            date: "28 Aug 2026",
            status: "Pending",
        },
        {
            name: "Michael John",
            age: 39,
            condition: "Back Pain",
            date: "27 Aug 2026",
            status: "In progress",
        },
    ];

    const filteredPatients = patients.filter((patient) => {

        const matchesStatus =
            selectedFilter === "All" ||
            patient.status === selectedFilter;

        const matchesSearch =
            patient.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
            patient.condition.toLowerCase().includes(searchTerm.toLowerCase());

        return matchesStatus && matchesSearch;
    });

    return (
        <div className="patient-section">

            {/* Filter + Search */}
            <div className="patient-controls">

                <div className="filter-container">

                    <button
                        className={`filter-button ${
                            showFilter ? "filter-active" : ""
                        }`}
                        onClick={() => setShowFilter(!showFilter)}
                    >
                        <span>⚱</span>
                        Filter
                    </button>

                    {showFilter && (
                        <div className="filter-options">

                            {["All", "Pending", "In progress", "Done"].map(
                                (option) => (
                                    <button
                                        key={option}
                                        className={
                                            selectedFilter === option
                                                ? "filter-option selected"
                                                : "filter-option"
                                        }
                                        onClick={() => {
                                            setSelectedFilter(option);
                                            setShowFilter(false);
                                        }}
                                    >
                                        {option}
                                    </button>
                                )
                            )}

                        </div>
                    )}

                </div>

                {/* Search */}
                <div className="search-container">

                    <span className="search-icon">⌕</span>

                    <input
                        type="text"
                        placeholder="Search patients..."
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                    />

                </div>

            </div>


            {/* Patient Table */}
            <div className="patient-table-container">

                <table>

                    <thead>
                        <tr>
                            <th>Patient</th>
                            <th>Age</th>
                            <th>Condition</th>
                            <th>Date</th>
                            <th>Status</th>
                            <th>Action</th>
                        </tr>
                    </thead>

                    <tbody>

                        {filteredPatients.map((patient, index) => (

                            <tr key={index}>

                                <td>{patient.name}</td>
                                <td>{patient.age}</td>
                                <td>{patient.condition}</td>
                                <td>{patient.date}</td>

                                <td>
                                    <span
                                        className={`status ${patient.status
                                            .toLowerCase()
                                            .replace(" ", "-")}`}
                                    >
                                        {patient.status}
                                    </span>
                                </td>

                                <td>
                                    <button className="action-button">
                                        {patient.status === "Pending"
                                            ? "Start"
                                            : "View"}
                                    </button>
                                </td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            </div>

        </div>
    );
}

export default PatientTable;