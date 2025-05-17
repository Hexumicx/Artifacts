import React from 'react';
import { useContext } from 'react';
import { UserContext } from '../UserContext';
import styles from './command.module.css';

function Commands() {
  const user_info = useContext(UserContext);
  const backend = process.env.REACT_APP_BACKEND;
  const sendCommand = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());
    data.name = user_info.name;
    fetch(`${backend}/add`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json'
      },
      body: JSON.stringify(data)
    })
  }
  return (
    <div className="command-center">
      <div>Actions</div>
      <form className={styles.action_form} onSubmit={sendCommand}>
        <label htmlFor="action">Move: </label>
        <input type="text" name="x" placeholder="X coordinate" className={styles.action_input} />
        <input type="text" name="y" placeholder="Y coordinate" className={styles.action_input} />
        <input type="hidden" name="action" value="move"/>
        <button type="submit" className={styles.action_button}>Submit</button>
      </form>
      <form className={styles.action_form} onSubmit={sendCommand}>
        <label htmlFor="action">Attack: </label>
        <input type="hidden" name="action" value="attack"/>
        <button type="submit" className={styles.action_button}>Submit</button>
      </form>
      <form className={styles.action_form} onSubmit={sendCommand}>
        <label htmlFor="action">Gather: </label>
        <input type="hidden" name="action" value="gather"/>
        <button type="submit" className={styles.action_button}>Submit</button>
      </form>
    </div>
  )
}

export default Commands;