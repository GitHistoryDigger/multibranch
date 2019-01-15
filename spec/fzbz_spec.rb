#!/usr/bin/env ruby -wKU

require_relative "../fzbz"

describe FizzBuzz do
  before :context do
    @obj = FizzBuzz.new(0)
  end
  (0...100).to_a.each { |n|
    it "FizzBuzz test (n=#{n})" do
      exp = "FizzBuzz" if n % 3 == 0 && n % 5 == 0
      exp = "Fizz" if n % 3 == 0 && n % 5 != 0
      exp = "Buzz" if n % 3 != 0 && n % 5 == 0
      exp = n.to_s if (exp || "").empty?
      expect(@obj.()).to eq exp
    end
  }
end
