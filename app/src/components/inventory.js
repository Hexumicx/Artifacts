import React from "react";
import { useContext } from 'react';
import { UserContext } from '../UserContext';
import styles from './inventory.module.css';

function Inventory() {
  const user_info = useContext(UserContext);
  const useritem1_10 = user_info ? user_info.inventory.slice(0, 10) : null;
  const useritem11_20 = user_info ? user_info.inventory.slice(10, 20) : null;
  const useritem1_10_list = useritem1_10 ? useritem1_10.map((item) => (
    item.code ? <li key={item.slot} className={styles.user_item}>
      <img src={`https://www.artifactsmmo.com/images/items/${item.code}.png`} alt='' />
      <p>{item.name}</p>
      </li> : <></>
  )) : null;
  const useritem11_20_list = useritem11_20 ? useritem11_20.map((item) => (
    item.code ? <li key={item.slot} className={styles.user_item}><img src={`https://www.artifactsmmo.com/images/items/${item.code}.png`} alt='' /></li> : <></>
  )) : null;

  return (
    <>
      <p>Inventory</p>
      <ul className={styles.user_item_list_row}>
        {useritem1_10_list}
      </ul>
      <ul className={styles.user_item_list_row}>
        {useritem11_20_list}
      </ul>
    </>
  );
}

export default Inventory;