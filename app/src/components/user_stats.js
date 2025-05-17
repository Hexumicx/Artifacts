import styles from './user_stats.module.css';
import { useContext } from 'react';
import { UserContext } from '../UserContext';

function UserStats() {
  const user_info = useContext(UserContext);
  return (
    <div className={styles.user_stats}>
      <div className={styles.stat_item}>Level: {user_info ? user_info.level : 'Loading...'}</div>
      <div className={styles.stat_item}>
        <span className={styles.main_stat_name}>HP:</span> 
        {user_info ? <Bar current={user_info.hp} max={user_info.max_hp} /> : <Bar current={0} max={0} />}
        <span className={styles.main_stat_ratio}>{user_info ? user_info.hp : 'loading...'}/{user_info ? user_info.max_hp : 'loading...'}</span>
      </div>
      <div className={styles.stat_item}>
        <span className={styles.main_stat_name}>XP:</span> 
        {user_info ? <Bar current={user_info.xp} max={user_info.max_xp} /> : <Bar current={0} max={0} />}
        <span className={styles.main_stat_ratio}>{user_info ? user_info.xp : 'loading...'}/{user_info ? user_info.max_xp : 'loading...'}</span>
      </div>
      <div style={{display: 'flex', flexDirection: 'row'}}>
        <div style={{marginRight: '25%'}} className={styles.stat_item}>
          Damage: {user_info ? user_info.dmg : 'loading...'}
        </div>
        <div className={styles.stat_item}>
          Crit: {user_info ? user_info.critical_strike : 'loading...'}
        </div>
      </div>
      <div style={{marginTop: '1%'}} className={styles.stat_item}>
        <div style={{marginRight: '20%'}}>
          <div>
            Damage Air: {user_info ? user_info.dmg_air : 'loading...'}
          </div>
          <div>
            Damage Earth: {user_info ? user_info.dmg_earth : 'loading...'}
          </div>
          <div>
            Damage Fire: {user_info ? user_info.dmg_fire : 'loading...'}
          </div>
          <div>
            Damage Water: {user_info ? user_info.dmg_water : 'loading...'}
          </div>
        </div>
        <div>
          <div>
            Resistance Air: {user_info ? user_info.res_air : 'loading...'}
          </div>
          <div>
            Resistance Earth: {user_info ? user_info.res_earth : 'loading...'}
          </div>
          <div>
            Resistance Fire: {user_info ? user_info.res_fire : 'loading...'}
          </div>
          <div>
            Resistance Water: {user_info ? user_info.res_water : 'loading...'}
          </div>
        </div>
      </div>

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
export default UserStats;