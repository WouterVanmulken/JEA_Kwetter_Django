import {Injectable} from '@angular/core';
import {Http} from '@angular/http';
import {Observable} from 'rxjs/Observable';
import {Tweet} from './tweet';
import 'rxjs/add/operator/map';
import {API_URL} from './constants';
import {Headers, RequestOptions} from '@angular/http';

@Injectable()
export class TweetService {


  constructor(private http: Http) {

  }

  personalTweets(userId: number): Observable<Tweet[]> {
    return this.http.get(`${API_URL}/personaltweets/${userId}/`)
      .map(response => response.json().results);
  }

  postTweet(userId: number, content: string): Observable<Tweet> {

    const payload = `{ \"content\": \"${content}\",\"poster\": \"http://127.0.0.1:8000/accounts/${userId}/\"  }`;
    console.log(payload);
    console.log(`${API_URL}/tweets/`);

    const headers = new Headers({ 'Content-Type': 'application/json' });
    const options = new RequestOptions({ headers: headers });


    return this.http.post(`${API_URL}/tweets/`, payload, options)
      .map(response => response.json());
  }

  //
  // toggleHeart(tweetId: number, userId: number) {
  //   this.http.get(`${API_URL}/tweets/heart/${tweetId}?userId=${userId}`)
  //     .subscribe();
  // // }
  getTweetsByUserId(id: number): Observable<Tweet[]> {
    return this.http.get(`${API_URL}tweets/?poster=${id}`)
      .map(response => response.json().results);
  }
}
