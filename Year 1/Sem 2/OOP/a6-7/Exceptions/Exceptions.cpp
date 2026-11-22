
#include "Exceptions.h"


Exceptions::Exceptions(string message){
  this->message = message;
}

const char* Exceptions::what() const noexcept{
  return this->message.c_str();
}

ExceptionsValidator::ExceptionsValidator(string message) : Exceptions(std::move(message)) {

}

ExceptionsRepository::ExceptionsRepository(string message) : Exceptions(std::move(message)) {

}