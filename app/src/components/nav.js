import styles from './nav.module.css';

function Nav({userList, setSelectedUser}) {
  const tabs = userList.map((user) => (
    <li key={user.name} className={styles.navitem} onClick={() => setSelectedUser(user.name)}>
      <div>{user.name}</div>
    </li>
  ));
  return (
    <div className={styles.nav}>
      <ul className={styles.navlist}>
        {tabs}
      </ul>
    </div>
  );
}

export default Nav;