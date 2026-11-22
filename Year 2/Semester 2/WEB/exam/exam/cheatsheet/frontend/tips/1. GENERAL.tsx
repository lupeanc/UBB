// GYM2: dropdown + table
// 2020EX1: form
// RECEPIES: checkboxes

import { useEffect, useState } from "react";

const func = () => {};
const [val, setVal] = useState("");
const [list, setList] = useState<any[]>([]);
const [miniList, setMiniList] = useState<any[]>([]);

//BUTTON
<button
  type="submit"
  onClick={(e) => {
    e.preventDefault();
    func();
  }}
>
  BUTTON
</button>;

//DROPDOWN
<select value={val} onChange={(e) => setVal(e.target.value)}>
  <option>CHOOSE</option>
  {list.map((c) => (
    <option value={c.id}>
      {c.id} - {c.className}: {c.classDate}
    </option>
  ))}
</select>;

//TABLE
<table>
  <thead>
    <tr>
      <th>Class ID</th>
      <th>Class Name</th>
      <th>Instructor Name</th>
      <th>Date</th>
      <th>Capacity</th>
    </tr>
  </thead>
  <tbody>
    {list.map((c) => (
      <>
        <tr>
          <td>{c.id}</td>
          <td>{c.className}</td>
          <td>{c.instructorName}</td>
          <td>{c.classDate}</td>
          <td>{c.maxCapacity}</td>
        </tr>
      </>
    ))}
  </tbody>
</table>;

//FORM
<form onSubmit={(e) => e.preventDefault()}>
  <label>ID:</label>
  <input value={val} readOnly></input>
  <label>User:</label>
  <input value={val} onChange={(e) => setVal(e.target.value)}></input>
  <label>Journal ID:</label>
  <input value={val} onChange={(e) => setVal(e.target.value)} />
  <label>Summary:</label>
  <input value={val} onChange={(e) => setVal(e.target.value)}></input>
  <label>Date:</label>
  <input value={val} onChange={(e) => setVal(e.target.value)}></input>
  <br></br>
  <label>Journal Name:</label>
  <input value={val} onChange={(e) => setVal(e.target.value)}></input>
</form>;

//CHECKBOXES
// list contains list like obj => mini lists
// list = [{minilist...}, {minilist...}, ...]

{
  list.map((i) => (
    <>
      <input
        type="checkbox"
        name={i.name}
        checked={miniList.includes(i.name)}
        onChange={(e) => handleChange(i, e.target.checked)}
      />
      {i.name}
    </>
  ));
}

const handleChange = (ingredient: any, checked: boolean) => {
  if (checked) {
    setMiniList((prev) => [...prev, " ", ingredient.name]);
  } else {
    setMiniList((prev) => prev.filter((i) => i != ingredient.name));
  }
};
