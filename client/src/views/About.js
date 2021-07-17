import React, { Component } from "react";


export default class About extends Component {
  constructor() {
    super();
    this.state = { users: [] };
  }

  async componentDidMount() {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    const json = await response.json();
    this.setState({ users: json });
  }

  render() {
    return (
        <div>
            <span>It is about page...</span>
            <ul>
              {
                this.state.users.slice(0, 10).map(user => (
                  <li>
                    { user.name }
                  </li>
                ))
              }
            </ul>
        </div>
    );
  }
}
