import {Component, OnInit} from '@angular/core';
import {Tweet} from '../tweet';
import {Account} from '../account';
import {TweetService} from '../tweet.service';
import {AccountService} from '../account.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  postContent: string;
  userName: string;
  // account: Account;
  accountId: number;
  tweets: Tweet[];
  loggedIn: number;

  constructor(private tweetService: TweetService, private accountService: AccountService) {
    this.userName = 'wouterv';
    this.loggedIn = 1;
  }


  ngOnInit() {
    this.accountId = 1;
    this.getCurrentAccount();
  }

  public getCurrentAccount() {
    // this.accountService.findByUsername(this.userName)
    //   .subscribe(account => {
    //     this.account = account;
    //     this.getTweetsByCurrentAccount();
    this.getPersonalTweets();
    //   });
  }

  // public getTweetsByCurrentAccount() {
  //   this.tweetService.getTweetsByUserId(this.account.id)
  //     .subscribe(tweets => this.account.tweets = tweets);
  // }

  public hasHearted(tweet: Tweet): boolean {

    for (let i = 0; i < tweet.hasLiked.length; i++) {
      const account = tweet.hasLiked[i];
      if (account.id === this.loggedIn) {
        return true;
      }
    }
    return false;

    // return false;
    // if (tweet.hearted == null) {
    //   return false;
    // }
    // for (let i = 0; i < tweet.hearted.length; i++) {
    //   const account = tweet.hearted[i];
    //   if (account.id == this.loggedIn) {
    //     return true;
    //   }
    // }
    // return false;
  }

  public post() {
    this.tweetService.postTweet(this.accountId, this.postContent)
      .subscribe(tweet => {
        tweet.poster = new Account(1, '', 'Wouter', 'Vanmulken', null, null, null);
        this.tweets.splice(0, 0, tweet);
      });
  }


  public getPersonalTweets() {
    this.tweetService.personalTweets(this.accountId)
      .subscribe(tweets => {
        console.log(tweets);
        this.tweets = tweets;
      });
  }

  public toggleHeart(tweet: Tweet) {
    // if (this.hasHearted(tweet)){
    //   const index = tweet.hearted.findIndex(x => x.id == this.loggedIn);
    //   tweet.hearted.splice(index, 1);
    // }else{
    //   const account: Account = <Account>{id : this.loggedIn};
    //   tweet.hearted.push(account);
    // }
    // this.tweetService.toggleHeart(tweet.id, this.account.id);
  }
}
