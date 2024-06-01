import { useState } from 'react';

interface ICard {
  id: number;
}
export function Card({ id }: ICard) {
  console.log(id);
  const [count, setCount] = useState(0);
  return (
    <div>
      <h1>Card {id}</h1>
      <p>count is {count}</p>
      <button onClick={() => setCount((prevcount) => prevcount + 1)}>increment</button>
    </div>
  );

}
