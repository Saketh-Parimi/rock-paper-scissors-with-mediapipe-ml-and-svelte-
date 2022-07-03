<script>
  import { onMount } from "svelte";

  let videoElement;
  let canvasElement;

  let canvasCtx;

  let currentLandmark;
  let lists = [];
  let classes = ["Rock", "Paper", "Scissors"];

  let className;
  let opponentsPick;

  let grid;
  let flag = false;

  let opponentsPickIndex;
  let whoWins;

  let scissors = [
    {
      x: 0.03628410026431084,
      y: 0.08913993090391159,
      z: 0.0311279296875,
    },
    {
      x: 0.00033595971763134,
      y: 0.07120539993047714,
      z: 0.0196380615234375,
    },
    {
      x: -0.01891135796904564,
      y: 0.049810152500867844,
      z: 0.0063323974609375,
    },
    {
      x: -0.030687205493450165,
      y: 0.024937918409705162,
      z: -0.0190887451171875,
    },
    {
      x: -0.02229265496134758,
      y: 0.00023806095123291016,
      z: -0.039276123046875,
    },
    {
      x: -0.026802126318216324,
      y: 0.0010265801101922989,
      z: 0.01226043701171875,
    },
    {
      x: -0.037063635885715485,
      y: -0.027459628880023956,
      z: 0.0053863525390625,
    },
    {
      x: -0.04789670929312706,
      y: -0.048826441168785095,
      z: 0.00010496377944946289,
    },
    {
      x: -0.05651812255382538,
      y: -0.06436318904161453,
      z: -0.019775390625,
    },
    {
      x: -0.00501288240775466,
      y: -0.005397092550992966,
      z: 0.0045013427734375,
    },
    {
      x: -0.012283625081181526,
      y: -0.04564175009727478,
      z: -0.00566864013671875,
    },
    {
      x: -0.019587036222219467,
      y: -0.06704346835613251,
      z: -0.021026611328125,
    },
    {
      x: -0.025610007345676422,
      y: -0.09255632758140564,
      z: -0.036529541015625,
    },
    {
      x: 0.01703629270195961,
      y: -0.0019523142836987972,
      z: -0.00815582275390625,
    },
    {
      x: -0.0015025025932118297,
      y: -0.007899625226855278,
      z: -0.03094482421875,
    },
    {
      x: -0.006992509588599205,
      y: 0.01535666361451149,
      z: -0.03656005859375,
    },
    {
      x: -0.005514351651072502,
      y: 0.038633838295936584,
      z: -0.032440185546875,
    },
    {
      x: 0.0339956060051918,
      y: 0.015279576182365417,
      z: -0.0163726806640625,
    },
    {
      x: 0.022487390786409378,
      y: 0.0013622306287288666,
      z: -0.0297088623046875,
    },
    {
      x: 0.007450649980455637,
      y: 0.007055139169096947,
      z: -0.040435791015625,
    },
    {
      x: 0.002702270168811083,
      y: 0.021796775981783867,
      z: -0.044647216796875,
    },
  ];

  let rock = [
    {
      x: 0.041055675595998764,
      y: 0.07757419347763062,
      z: 0.035888671875,
    },
    {
      x: 0.00548841618001461,
      y: 0.0693695992231369,
      z: 0.0238800048828125,
    },
    {
      x: -0.02406315878033638,
      y: 0.05049889534711838,
      z: 0.0186004638671875,
    },
    {
      x: -0.05241893604397774,
      y: 0.02876254916191101,
      z: 0.0032291412353515625,
    },
    {
      x: -0.06535016000270844,
      y: 0.002382071688771248,
      z: -0.003162384033203125,
    },
    {
      x: -0.02642267569899559,
      y: 0.007410014979541302,
      z: 0.00872802734375,
    },
    {
      x: -0.035985905677080154,
      y: 0.018316809087991714,
      z: -0.022430419921875,
    },
    {
      x: -0.02454761415719986,
      y: 0.034551359713077545,
      z: -0.0187835693359375,
    },
    {
      x: -0.016871195286512375,
      y: 0.03536348044872284,
      z: 0.00812530517578125,
    },
    {
      x: -0.004847875330597162,
      y: -0.003220499726012349,
      z: 0.0048065185546875,
    },
    {
      x: -0.016822751611471176,
      y: 0.007453267928212881,
      z: -0.03363037109375,
    },
    {
      x: -0.012235786765813828,
      y: 0.038161247968673706,
      z: -0.031982421875,
    },
    {
      x: -0.00020841415971517563,
      y: 0.03358671814203262,
      z: -0.0022411346435546875,
    },
    {
      x: 0.017125383019447327,
      y: -0.006716860458254814,
      z: -0.005523681640625,
    },
    {
      x: 0.007333923131227493,
      y: 0.010345753282308578,
      z: -0.036163330078125,
    },
    {
      x: 0.009669674560427666,
      y: 0.03503071516752243,
      z: -0.032623291015625,
    },
    {
      x: 0.01898261532187462,
      y: 0.029249560087919235,
      z: -0.006153106689453125,
    },
    {
      x: 0.036035120487213135,
      y: 0.005334596149623394,
      z: -0.0128631591796875,
    },
    {
      x: 0.02669435366988182,
      y: 0.010095085948705673,
      z: -0.036895751953125,
    },
    {
      x: 0.02599324658513069,
      y: 0.03196633607149124,
      z: -0.0411376953125,
    },
    {
      x: 0.03131629526615143,
      y: 0.02977634221315384,
      z: -0.0269317626953125,
    },
  ];

  let paper = [
    {
      x: 0.014842486940324306,
      y: 0.10195957124233246,
      z: -0.00005561113357543945,
    },
    {
      x: -0.014061728492379189,
      y: 0.07637865841388702,
      z: 0.0018224716186523438,
    },
    {
      x: -0.027308087795972824,
      y: 0.05075034499168396,
      z: -0.0029754638671875,
    },
    {
      x: -0.03914172574877739,
      y: 0.021637532860040665,
      z: -0.01177978515625,
    },
    {
      x: -0.0473976694047451,
      y: -0.00047681573778390884,
      z: -0.016693115234375,
    },
    {
      x: -0.022131353616714478,
      y: 0.0013116062618792057,
      z: 0.014678955078125,
    },
    {
      x: -0.026887398213148117,
      y: -0.029113413766026497,
      z: 0.00707244873046875,
    },
    {
      x: -0.03601223602890968,
      y: -0.04691984876990318,
      z: -0.00400543212890625,
    },
    {
      x: -0.04713686555624008,
      y: -0.05866580829024315,
      z: -0.028350830078125,
    },
    {
      x: -0.003181153442710638,
      y: -0.004543568938970566,
      z: 0.007076263427734375,
    },
    {
      x: -0.011760739609599113,
      y: -0.04031627997756004,
      z: -0.002643585205078125,
    },
    {
      x: -0.022903990000486374,
      y: -0.058958642184734344,
      z: -0.0192718505859375,
    },
    {
      x: -0.03735097125172615,
      y: -0.07580279558897018,
      z: -0.038726806640625,
    },
    {
      x: 0.014806762337684631,
      y: -0.002127537503838539,
      z: -0.00902557373046875,
    },
    {
      x: 0.006793047767132521,
      y: -0.030763104557991028,
      z: -0.0175628662109375,
    },
    {
      x: -0.0038462989032268524,
      y: -0.05041514337062836,
      z: -0.0323486328125,
    },
    {
      x: -0.01810586452484131,
      y: -0.06648789346218109,
      z: -0.048583984375,
    },
    {
      x: 0.025640035048127174,
      y: 0.014499043114483356,
      z: -0.0243072509765625,
    },
    {
      x: 0.025324292480945587,
      y: -0.010447743348777294,
      z: -0.0269012451171875,
    },
    {
      x: 0.016226589679718018,
      y: -0.030564820393919945,
      z: -0.037994384765625,
    },
    {
      x: 0.0035896049812436104,
      y: -0.0430014431476593,
      z: -0.052764892578125,
    },
  ];

  let opponentsLists = [];
  opponentsLists.push(rock);
  opponentsLists.push(paper);
  opponentsLists.push(scissors);

  onMount(async () => {
    try {
      canvasCtx = canvasElement.getContext("2d");

      function onResult(results) {
        canvasCtx.save();
        canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
        canvasCtx.drawImage(
          results.image,
          0,
          0,
          canvasElement.width,
          canvasElement.height
        );
        if (results.multiHandLandmarks) {
          for (const landmarks of results.multiHandLandmarks) {
            drawConnectors(canvasCtx, landmarks, HAND_CONNECTIONS, {
              color: "#00FF00",
              lineWidth: 5,
            });
            currentLandmark = landmarks;
            drawLandmarks(canvasCtx, landmarks, {
              color: "#FF0000",
              lineWidth: 2,
            });
          }
          // console.log(results.multiHandLandmarks);

          canvasCtx.restore();

          if (flag) {
            const landmarks = opponentsPick.reduce(
              (prev, current) => [...prev, ...current],
              []
            );
            // console.log(landmarks);
            const colors = [];
            let connections = [];
            for (let loop = 0; loop < opponentsPick.length; ++loop) {
              const offset = loop * HAND_CONNECTIONS.length;
              const offsetConnections = HAND_CONNECTIONS.map((connection) => [
                connection[0] + offset,
                connection[1] + offset,
              ]);
              connections = connections.concat(offsetConnections);
              const classification = opponentsPick[loop];
              colors.push({
                list: offsetConnections.map((_, i) => i + offset),
                color: classification.label,
              });
            }
            // console.log(results.multiHandLandmarks);
            grid.updateLandmarks(landmarks, connections, colors);
          }
          // console.log(results.multiHandLandmarks);
        }
      }

      const hands = new Hands({
        locateFile: (file) => {
          return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
        },
      });
      hands.setOptions({
        maxNumHands: 2,
        modelComplexity: 1,
        minDetectionConfidence: 0.5,
        minTrackingConfidence: 0.5,
      });
      hands.onResults(onResult);

      const camera = new Camera(videoElement, {
        onFrame: async () => {
          await hands.send({
            image: videoElement,
          });
        },
      });
      camera.start();
    } catch (e) {
      console.log(e);
    }
    const landmarkContainer = document.getElementsByClassName(
      "landmark-grid-container"
    )[0];
    grid = new LandmarkGrid(landmarkContainer, {
      connectionColor: 0xcccccc,
      definedColors: [
        { name: "Left", value: 0xffa500 },
        { name: "Right", value: 0x00ffff },
      ],
      range: 0.2,
      fitToGrid: false,
      labelSuffix: "m",
      landmarkSize: 2,
      numCellsPerAxis: 4,
      showHidden: false,
      centered: false,
    });
  });

  function buttonClicked() {
    flag = false;
    opponentsPickIndex = Math.floor(Math.random() * 3);
    lists = [];
    currentLandmark.forEach((element) => {
      lists.push(element["x"]);
      lists.push(element["y"]);
      lists.push(element["z"]);
    });

    axios
      .post("http://127.0.0.1:5000/", {
        body: { landmarks: lists },
        headers: { "Access-Control-Allow-Origin": true },
      })
      .then(function (response) {
        flag = true;
        className = response.data["class"];

        opponentsPick = [opponentsLists[opponentsPickIndex]];

        if (
          (classes[opponentsPickIndex] == "Rock" &&
            classes[className] == "Rock") ||
          (classes[opponentsPickIndex] == "Paper" &&
            classes[className] == "Paper") ||
          (classes[opponentsPickIndex] == "Scissors" &&
            classes[className] == "Scissors")
        )
          whoWins = "Tie!";
        else if (
          (classes[opponentsPickIndex] == "Rock" &&
            classes[className] == "Paper") ||
          (classes[opponentsPickIndex] == "Paper" &&
            classes[className] == "Scissors") ||
          (classes[opponentsPickIndex] == "Scissors" &&
            classes[className] == "Rock")
        )
          whoWins = "You Won!";
        else whoWins = "You Lose!";

        console.log(whoWins);
        console.log(opponentsLists[opponentsPickIndex]);
        console.log(classes[className]);
      })
      .catch(function (error) {
        console.log(error);
      });
  }
</script>

<main>
  <!-- svelte-ignore a11y-media-has-caption -->
  {#if classes[className]}
    <h1>Your Pick: {classes[className]}</h1>
  {/if}
  {#if classes[opponentsPickIndex]}
    <h1>His Pick: {classes[opponentsPickIndex]}</h1>
  {/if}
  {#if whoWins}
    <h2>{whoWins}</h2>
  {/if}

  <!-- svelte-ignore a11y-media-has-caption -->
  <video bind:this={videoElement} width="1280" height="720" hidden />

  <canvas bind:this={canvasElement} width="1000" height="600" />

  <button on:click={buttonClicked}>Click Me!</button>

  <div class="square-box">
    <div class="landmark-grid-container" />
  </div>
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
