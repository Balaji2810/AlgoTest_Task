import React, { useState, useEffect } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Form from "react-bootstrap/Form";

import helper from "./helper";
import storage from "./storage/storage";

import "bootstrap/dist/css/bootstrap.min.css";

export const Home = (props) => {
  useEffect(() => {
    helper.access().then((status) => {
      if (status) {
      } else {
        storage.remove("refresh");
        props.onFormSwitch("login");
      }
    });
  }, []);
  return (
    <div className="Home">
      <h1>HOME</h1>
      <Card />
    </div>
  );
};

const Card = () => {
  return (
    <Container fluid className="container">
      <Row>
        <Col>
          <p>Total Lots</p> <input type="number" className="card_input" />
        </Col>
        <Col>
          <p>Position</p>
          <Form.Select aria-label="Position Type">
            <option value="sell">Sell</option>
            <option value="buy">Buy</option>
          </Form.Select>
        </Col>
        <Col>
          <p>Option Type</p>
          <Form.Select aria-label="Option Type">
            <option value="call">Call</option>
          </Form.Select>
        </Col>
        <Col>
          <p>Total Lots</p>
          <Form.Select aria-label="Expiry">
            <option value="weekly">Weekly</option>
            <option value="monthly">Monthly</option>
          </Form.Select>
        </Col>
        <Col>
          <p>Select Strike Criteria</p>
          <Form.Select aria-label="Position Type">
            <option value="sell">Premium Range</option>
            <option value="sell">Strike Type</option>
            <option value="sell">Closest Premium</option>
            <option value="sell">Straddle Width</option>
          </Form.Select>
        </Col>
        <Col>
          <p>
            [ATM Strike{" "}
            <Form.Select aria-label="Position Type" size="sm" className="temp">
              <option value="+">+</option>
              <option value="+">-</option>
            </Form.Select>
            ( <input type="number" className="card_input" /> x ATM Straddle
            price)
          </p>
        </Col>
      </Row>
      <Row>
        <Col xs={2}></Col>
        <Col>
          <p>Simple Momentum</p>
          <div className="simple_momentum">
            <Form.Select aria-label="Expiry">
              <option value="points_up">Points ↑</option>
              <option value="points_down">Points ↓</option>
            </Form.Select>
            <input type="number" className="card_input" />
          </div>
        </Col>
        <Col>
          <p>Trail SL</p>
          <div className="trail_sl">
            <Form.Select aria-label="Expiry">
              <option value="points">Points</option>
              <option value="percentage">Percentage</option>
            </Form.Select>
            <input type="number" className="card_input" />
            <input type="number" className="card_input" />
          </div>
        </Col>
        <Col xs={2}></Col>
      </Row>
    </Container>
  );
};
