import {Component} from '@angular/core';
import {Observable} from 'rxjs';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'my-app';

  constructor(private http: HttpClient) {
    console.log('Constructing app component');
    this.getData();
  }

  public getData() {
    return this.http.get('/train').subscribe((data: any) => {
      console.log(data);
    });
  }
}
