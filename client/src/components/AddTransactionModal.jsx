import "./../style/modal.css";

export default function AddTransactionModal({
    children,
    onClose,
}) {

    return (

        <div
            className="modal-overlay"
            onClick={onClose}
        >

            <div
                className="modal"
                onClick={(e) => e.stopPropagation()}
            >

                <div className="modal-header">

                    <h2>Add Transaction</h2>

                    <button
                        className="close-btn"
                        onClick={onClose}
                    >
                        <i className="ti ti-x"></i>
                    </button>

                </div>

                {children}

            </div>

        </div>

    );

}