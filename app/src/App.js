import React from 'react';
import { useState } from 'react';
import Nav from './components/nav';
import User from './components/user';
import './App.css';

function App() {
  const userList = [
    { name: 'Wix1' },
    { name: 'Wix2' },
    { name: 'Wix3' },
    { name: 'Wix4' },
    { name: 'Wix5' },
  ];
  const [selectedUser, setSelectedUser] = useState(userList[0].name);
  return (
    <>
      <Nav setSelectedUser={setSelectedUser} userList={userList} />
      <div className='user-item'><User character_name={selectedUser}/></div>
    </>
  );
}

export default App;
