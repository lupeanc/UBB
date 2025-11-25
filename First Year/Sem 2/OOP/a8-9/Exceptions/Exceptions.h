
#ifndef EXCEPTIONS_H
#define EXCEPTIONS_H
#include <iostream>
#include <exception>
#include <utility>
using namespace std;
#pragma once

class Exceptions: public exception{
  protected:
    string message;
    public:
      explicit Exceptions(string message);
      [[nodiscard]] const char* what() const noexcept override;
};

class ExceptionsValidator: public Exceptions{
  public:
    explicit ExceptionsValidator(string message);
};

class ExceptionsRepository: public Exceptions{
  public:
    explicit ExceptionsRepository(string message);
};

#endif //EXCEPTIONS_H
