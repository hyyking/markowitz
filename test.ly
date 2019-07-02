
& Test (scale=100, precision=100)
{
    [       NormalGraph(peugeot) | NormalGraph(lvmh) | NormalGraph(renault) | NormalGraph(axa) | NormalGraph(airliquide)]
    [       EfficientFrontier(peugeot/lvmh) | EfficientFrontier(renault/peugeot/axa) | EfficientFrontier(axa/airliquide) ]
    [       EfficientFrontier(peugeot/axa) | EfficientFrontier(renault/axa) ]
}




