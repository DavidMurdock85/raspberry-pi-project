import React, { useEffect, useState } from "react";
import axios from "axios";

const App: React.FC = () => {
  const [numbers, setNumbers] = useState<number[]>([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/api/numbers")
      .then((response) => {
        setNumbers(response.data);
      })
      .catch((error) => {
        console.error("There was an error fetching the numbers!", error);
      });
  }, []);

  return (
    <div className="App">
      <h2>even numbers</h2>
      <ul>
        {numbers.map((number, index) => {
          if (number % 2 === 0) {
            return <li key={index}>{number}</li>;
          } else {
            return null;
          }
        })}
      </ul>

      <h2>odd numbers</h2>
      <ul>
        {numbers.map((number, index) => {
          if (number % 2 !== 0) {
            return <li key={index}>{number}</li>;
          } else {
            return null; // or omit the else block if you prefer
          }
        })}
      </ul>

    </div>
  );
};

export default App;
