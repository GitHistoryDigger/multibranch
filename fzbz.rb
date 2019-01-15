#!/usr/bin/env ruby -wKU

class FizzBuzz
  def initialize(init=0)
    @num = init
  end
  def call()
    ret = []
    if @num % 3 == 0
      ret << "Fizz"
    end
    if @num % 5 == 0
      ret << "Buzz"
    end
    ret << @num.to_s if ret.empty?
    @num += 1
    ret.join()
  end
end
