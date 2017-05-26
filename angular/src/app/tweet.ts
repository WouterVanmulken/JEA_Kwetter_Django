import {Account} from './account';
export class Tweet {
  constructor(public id: number,
              public content: string,
              public timestamp: Date,
              public poster: Account,
              public hasLiked: Account[]) {
  }
}
