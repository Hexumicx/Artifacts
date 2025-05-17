import styles from './user.module.css';
import { useState, useEffect } from 'react';
import { UserContext } from '../UserContext';
import UserStats from './user_stats';
import UserSkills from './user_skills';
import Inventory from './inventory';
import Commands from './command';

function User(props) {
  const [user_info, setUserInfo] = useState(null);
  const [refresh, setRefresh] = useState(false);
  useEffect(() => {
    const fetchUserInfo = async () => {
      const data = await retreiveUserInfo(props.character_name);
      setUserInfo(data);
    }
    fetchUserInfo();
  }, [refresh, props.character_name]);

  return (
    <UserContext.Provider value={user_info}>
      <div className={styles.user_component}>
        <div className={styles.left}>
          <div className={styles.header}>
            <p>Character Name: {props.character_name}</p>
            <button onClick={() => setRefresh(!refresh)}>Refresh</button>
          </div>
          <UserStats/>
          <UserSkills/>
          <Inventory/>
          <div>
            Equipment:
          </div>
          <div className={styles.actions}>
            <form className={styles.action_form}>
              <input type="text" placeholder="Action" className={styles.action_input} />
              <input type="text" placeholder="Target" className={styles.action_input} />
              <button type="submit" className={styles.action_button}>Submit</button>
            </form>
          </div>
        </div>
        <div className={styles.right}>
          <Commands />
        </div>
      </div>
    </UserContext.Provider>
  );
}

async function retreiveUserInfo(character_name) {
  const server = process.env.REACT_APP_SERVER
  const USERID = process.env.REACT_APP_USERID
  const url = `${server}/accounts/${USERID}/characters`;
  const options = {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      Accept: 'application/json'
    }
  };

  try {
    const response = await fetch(url, options);
    if (!response.ok) {
      throw response.status;
    }
    const data = await response.json();
    const char_data = data.data.find((character) => character.name === character_name);
    return char_data;
  } catch (error) {
    console.error('Error fetching user info:', error);
  }
}

export default User;