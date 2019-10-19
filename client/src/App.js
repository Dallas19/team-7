import React, { useState } from "react";

import Button from "react-bootstrap/Button";
import Dropzone from "react-dropzone";

import "./App.css";

const App = () => {
  const [studentFileName, setStudentFileName] = useState(
    "Drag or Click to Browse File"
  );
  const [companyFileName, setCompanyFileName] = useState(
    "Drag or Click to Browse File"
  );

  return (
    <div className="App">
      <header className="App-header">
        <h1> Auto Matcher </h1>
        <h4>Student Ranking File</h4>
        <Dropzone
          className="Dropzone"
          onDrop={acceptedFiles => setStudentFileName(acceptedFiles[0].name)}
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
          onDrop={acceptedFiles => setCompanyFileName(acceptedFiles[0].name)}
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
          <Button className="Button"> Interviews </Button>
          <Button className="Button"> Offers </Button>
        </div>
      </header>
    </div>
  );
};

export default App;
