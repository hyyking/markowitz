# This is a comment

& non_scaled_low_prec (precision=10)
{
    [ NormalGraph(axa) | NormalGraph(peugeot) | NormalGraph(lvmh) ]

    [                    EfficientFrontier(axa/peugeot/lvmh)      ]

}


& scaled (precision=1000, scale=100)
{
    [ NormalGraph(axa) | NormalGraph(peugeot) | NormalGraph(lvmh) ]

    [                    EfficientFrontier(axa/peugeot/lvmh)      ]

}


& scaled_new_line (scale=100, line=g--)
{
    [ NormalGraph(axa) | NormalGraph(peugeot) | NormalGraph(lvmh) ]

    [                    EfficientFrontier(axa/peugeot/lvmh)      ]

}


& mult_on_one (scale=100)
{
    [ NormalGraph(axa) NormalGraph(peugeot) | NormalGraph(peugeot) | NormalGraph(lvmh) ]

    [                    EfficientFrontier(axa/peugeot/lvmh)      ]

}





