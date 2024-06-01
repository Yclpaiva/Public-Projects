import '@testing-library/jest-dom'
import { soma } from '../services/soma';

describe('soma', () => {
  it('deve retornar 2 quando 1 ', () => {
    const resultado = soma(1);
    expect(resultado).toBe(2);
  });

  it('deve retornar 3 quando 2', () => {
    const resultado = soma(2);
    expect(resultado).toBe(3);
  });

  it('deve retornar 4 quando 3', () => {
    const resultado = soma(3);
    expect(resultado).toBe(4);
  });
})
