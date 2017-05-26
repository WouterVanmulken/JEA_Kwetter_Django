import {Tweet} from './tweet';
export class Account {
  constructor(public id: number,
              public bio: string,
              public first_name: string,
              public last_name: string,
              public tweets?: Tweet[],
              public following?: Account[],
              public followers?: Account[]) {
  }
}
