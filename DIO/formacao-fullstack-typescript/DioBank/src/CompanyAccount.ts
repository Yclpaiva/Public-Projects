import { PlatformAccount } from "./PlatformAccount"

export class CompanyAccount extends PlatformAccount {

  constructor(name: string, accountNumber: number) {
    super(name, accountNumber)
  }

  getLoan = (value: number): void => {
    if (this.validateStatus()) {
      this.balance += value
      console.log('Voce pegou um empréstimo')
    }
  }
}
