import { useContext } from 'react';
import { UserContext } from '../UserContext';
import styles from './user_skills.module.css';

function User_skills() {
  const skills = ['mining', 'woodcutting', 'fishing', 'weaponcrafting', 'gearcrafting', 'jewelrycrafting', 'cooking', 'alchemy']
  const user_info = useContext(UserContext);
  const skill_list = skills.map((skill) => (
    <div key={skill} className={styles.skill_item}>
      <span className={styles.skill_name}>{skill.charAt(0).toUpperCase() + skill.slice(1)}:</span> 
      {user_info ? <Bar current={user_info[`${skill}_xp`]} max={user_info[`${skill}_max_xp`]} /> : <Bar current={0} max={0} />}
      <span style={{width:'100px', display:'flex', justifyContent:'flex-end'}}>{user_info ? user_info[`${skill}_xp`] : 'loading...'}/{user_info ? user_info[`${skill}_max_xp`] : 'loading...'}</span>
    </div>
  ));
  return (
    <div className={styles.user_skills}>
      {skill_list}
    </div>
  );
}

function Bar({current, max}) {
  const ratio = current / max;
  return (
    <div className={styles.bar_container}>
      <div className={styles.bar}>
        <div className={styles.bar_fill} style={{ width: `${ratio * 100}%` }}></div>
      </div>
    </div>
  );
}

export default User_skills;