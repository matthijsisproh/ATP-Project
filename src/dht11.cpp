#include <iostream>

class DHT11{
    public:
    void update(){
        _value += 1;

    }

    float read_value(){
        return _value;

    }

    char measure(){
        return _unit_of_measure;

    }

    float _convert_to_value(){
        return _value;
    }

    float return_value(){
        return _value;
    }

    private:
    int _value = 0;
    char _unit_of_measure = 'c';
};

int main(){
    std::cout << "Hello world!";
}