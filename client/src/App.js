import React, { useState } from "react";

import Button from "react-bootstrap/Button";
import Dropzone from "react-dropzone";

import axios from "axios";

import "./App.css";

// file drop/upload
const App = () => {
  const [studentFileName, setStudentFileName] = useState(
    "Drag or Click to Browse File"
  );
  const [companyFileName, setCompanyFileName] = useState(
    "Drag or Click to Browse File"
  );

  // defining pairs of files
  const [studentFile, setStudentFile] = useState();
  const [companyFile, setCompanyFile] = useState();

  const files = [studentFile, companyFile];

  // http post using axios
  const handleSubmit = theFiles => {
    console.log(theFiles);
    axios
      .post(`http://127.0.0.1:5000/getInterviewSchedule`, theFiles)
      .then(res => {
        console.log(res);
        console.log(res.data);
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1> Auto Matcher </h1>
        <h4>Student Ranking File</h4>
        <Dropzone
          className="Dropzone"
          onDrop={acceptedFiles => {
            setStudentFile(acceptedFiles[0]);
            setStudentFileName(acceptedFiles[0].name);
          }}
        >
          {({ getRootProps, getInputProps }) => (
            <section>
              <div {...getRootProps()}>
                <input {...getInputProps()} />
                <p>{studentFileName}</p>
              </div>
            </section>
          )}
        </Dropzone>
        <h4>Company Ranking File</h4>
        <Dropzone
          className="Dropzone"
          onDrop={acceptedFiles => {
            setCompanyFile(acceptedFiles[0]);
            setCompanyFileName(acceptedFiles[0].name);
          }}
        >
          {({ getRootProps, getInputProps }) => (
            <section>
              <div {...getRootProps()}>
                <input {...getInputProps()} />
                <p>{companyFileName}</p>
              </div>
            </section>
          )}
        </Dropzone>
        <div>
          <Button
            disabled={!files[0] || !files[1]}
            className="Button"
            onClick={() => handleSubmit(files)}
          >Interviews </Button>
          <Button 
            disabled={!files[0] || !files[1]}
            className="Button"> Offers </Button>
        </div>
      </header>
    </div>
  );
};

export default App;
